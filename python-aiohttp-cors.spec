%define module aiohttp-cors
%define oname aiohttp_cors
# disable test for abf.
%bcond_with test

Name:		python-aiohttp-cors
Version:	0.8.1
Release:	1
Summary:	CORS support for aiohttp
URL:		https://pypi.org/project/aiohttp-cors/
License:	Apache-2.0
Group:		Development/Python
Source0:	https://files.pythonhosted.org/packages/source/a/aiohttp-cors/%{oname}-%{version}.tar.gz
BuildSystem:	python
BuildArch:	noarch

BuildRequires:	python
BuildRequires:  pkgconfig(python3)
BuildRequires:	python%{pyver}dist(setuptools)
%if %{with test}
BuildRequires:	python%{pyver}dist(aiohttp)
BuildRequires:	python%{pyver}dist(aiosignal)
BuildRequires:	python%{pyver}dist(async-timeout)
BuildRequires:	python%{pyver}dist(attrs)
BuildRequires:	python%{pyver}dist(chardet)
BuildRequires:	python%{pyver}dist(idna)
BuildRequires:	python%{pyver}dist(multidict)
BuildRequires:	python%{pyver}dist(pytest-asyncio)
BuildRequires:	python%{pyver}dist(pytest-mock)
BuildRequires:	python%{pyver}dist(pytest-trio)
BuildRequires:	python%{pyver}dist(selenium)
BuildRequires:	python%{pyver}dist(yarl)
%endif
Requires:	python%{pyver}dist(aiohttp) >= 3.9

%description
CORS support for aiohttp.

aiohttp_cors library implements Cross Origin Resource Sharing (CORS) support
for aiohttp asyncio-powered asynchronous HTTP server.

%prep
%autosetup -p1 -n %{oname}-%{version}
# remove code coverage flags from pytest
sed -i '/addopts/d' setup.cfg

%build
%py_build

%install
%py3_install

%if %{with test}
%check
%{__python} -m pytest -v tests/unit --ignore tests/integration/test_real_browser.py
%endif

%files
%{python3_sitelib}/%{oname}
%{python3_sitelib}/%{oname}-%{version}-*.*-info
%license LICENSE
%doc README.rst