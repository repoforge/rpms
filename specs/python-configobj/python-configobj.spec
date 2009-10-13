# $Id$
# Authority: dag
# Upstream: Michael Foord & Nicola Larosa <fuzzyman$voidspace,org,uk>

%define python_sitelib %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib()')

%define real_name configobj

Summary: Config file reading, writing, and validation
Name: python-configobj
Version: 4.6.0
Release: 1
License: BSD
Group: System Environment/Libraries
URL: http://www.voidspace.org.uk/python/configobj.html

Source: http://www.voidspace.org.uk/downloads/configobj-%{version}.zip
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: python-devel
BuildRequires: python-setuptools

%description
ConfigObj is a simple but powerful config file reader and writer: an ini file
round tripper. Its main feature is that it is very easy to use, with a
straightforward programmer's interface and a simple syntax for config files.

%prep
%setup -n %{real_name}-%{version}

%build
%{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root="%{buildroot}" --prefix="%{_prefix}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc docs/
%{python_sitelib}/configobj.py
%{python_sitelib}/configobj.pyc
%{python_sitelib}/configobj.pyo
%{python_sitelib}/validate.py
%{python_sitelib}/validate.pyc
%{python_sitelib}/validate.pyo
#%{python_sitelib}/configobj-%{version}-py*.egg-info

%changelog
* Tue Oct 13 2009 Steve Huff <shuff@vecna.org> - 4.6.0-1
- Updated to release 4.6.0.

* Thu Dec 11 2008 Dag Wieers <dag@wieers.com> - 4.5.3-1
- Initial package. (based on fedora)
