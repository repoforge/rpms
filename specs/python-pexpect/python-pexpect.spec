# $Id$
# Authority: dag

%define python_sitelib %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib()')

%define real_name pexpect

Summary: Python Expect-like module
Name: python-pexpect
Version: 2.0
Release: 1
License: Python Software Foundation License
Group: Development/Libraries
URL: http://pexpect.sourceforge.net/

Source: http://dl.sf.net/pexpect/pexpect-%{version}.tgz
Source1: http://dl.sf.net/pexpect/pexpect-%{version}-examples.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: python-devel >= 2.0

%description
Pexpect is a pure Python module for spawning child applications; controlling
them; and responding to expected patterns in their output.

Pexpect can be used for automating interactive applications such as ssh, ftp,
passwd, telnet, etc. It can be used to a automate setup scripts for duplicating
software package installations on different servers. It can be used for
automated software testing.

%prep
%setup -n %{real_name}-%{version} -a 1

%{__rm} -rf examples/CVS/

%build
%{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root="%{buildroot}" --prefix="%{_prefix}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README examples/
%{python_sitelib}/pexpect.py
%{python_sitelib}/pexpect.pyc
%ghost %{python_sitelib}/pexpect.pyo

%changelog
* Sun Nov 27 2005 Dag Wieers <dag@wieers.com> - 2.0-1
- Initial package. (using DAR)
