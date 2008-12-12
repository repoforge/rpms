# $Id$
# Authority: dag

%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')

%define real_name pylirc

Summary: Linux Infrared Remote Control python module
Name: python-lirc
Version: 0.0.5
Release: 1
License: GPL
Group: Development/Languages
URL: http://pylirc.mccabe.nu/

Source: http://dl.sf.net/pylirc/pylirc-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: lirc-devel
BuildRequires: python-devel
Obsoletes: pylirc <= %{version}-%{release}
Provides: pylirc = %{version}-%{release}

%description
pyLirc is a module for Python that interacts with lirc to give Python programs
the ability to receive commands from remote controls.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root="%{buildroot}" --prefix="%{_prefix}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc PKG-INFO
%{python_sitearch}/pylircmodule.so

%changelog
* Thu Dec 11 2008 Dag Wieers <dag@wieers.com> - 0.0.5-1
- Initial package. (based on fedora)
