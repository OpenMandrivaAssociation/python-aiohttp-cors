%define module aiohttp-cors
%define oname aiohttp_cors
# disable test for abf.
%bcond test 0

Name:		python-aiohttp-cors
Version:	0.8.1
Release:	2
Summary:	CORS support for aiohttp
URL:		https://pypi.org/project/aiohttp-cors/
License:	Apache-2.0
Group:		Development/Python
Source0:	https://files.pythonhosted.org/packages/source/a/aiohttp-cors/%{oname}-%{version}.tar.gz
BuildSystem:	python
BuildArch:	noarch

BuildRequires:	pkgconfig
BuildRequires:  pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)
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
# Remove bundled egg-info
rm -rf %{oname}.egg-info
# remove code coverage flags from pytest
sed -i '/addopts/d' setup.cfg

%build
%py_build

%install
%py_install

%if %{with test}
%check
export CI=true
export PYTHONPATH="%{buildroot}%{python_sitearch}:${PWD}"
pytest -v tests/unit --ignore tests/integration/test_real_browser.py
%endif

%files
%{python_sitelib}/%{oname}
%{python_sitelib}/%{oname}-%{version}-*.*-info
%license LICENSE
%doc README.rst
