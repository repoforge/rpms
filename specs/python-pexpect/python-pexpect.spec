# $Id$
# Authority: dag

%define python_sitelib %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib()')

%define real_name pexpect

Summary: Python Expect-like module
Name: python-pexpect
Version: 2.3
Release: 1
License: Python Software Foundation License
Group: Development/Libraries
URL: http://pexpect.sourceforge.net/

Source: http://dl.sf.net/pexpect/pexpect-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: python-devel >= 2.0

Obsoletes: pexpect <= %{version}-%{release}
Provides: pexpect = %{version}-%{release}

%description
Pexpect is a pure Python module for spawning child applications; controlling
them; and responding to expected patterns in their output.

Pexpect can be used for automating interactive applications such as ssh, ftp,
passwd, telnet, etc. It can be used to a automate setup scripts for duplicating
software package installations on different servers. It can be used for
automated software testing.

%prep
%setup -n %{real_name}-%{version}

%build
%{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root="%{buildroot}" --prefix="%{_prefix}"

### Clean up docs
%{__mv} -f ANSI.py FSM.py screen.py examples/
find examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc LICENSE README doc/ examples/
%{python_sitelib}/fdpexpect.py
%{python_sitelib}/fdpexpect.pyc
%ghost %{python_sitelib}/fdpexpect.pyo
%{python_sitelib}/pexpect.py
%{python_sitelib}/pexpect.pyc
%ghost %{python_sitelib}/pexpect.pyo
%{python_sitelib}/pxssh.py
%{python_sitelib}/pxssh.pyc
%ghost %{python_sitelib}/pxssh.pyo
%{python_sitelib}/ANSI.py
%{python_sitelib}/ANSI.pyc
%ghost %{python_sitelib}/ANSI.pyo
%{python_sitelib}/FSM.py
%{python_sitelib}/FSM.pyc
%ghost %{python_sitelib}/FSM.pyo
%{python_sitelib}/screen.py
%{python_sitelib}/screen.pyc
%ghost %{python_sitelib}/screen.pyo

%changelog
* Tue Apr  7 2009 Dries Verachtert <dries@ulyssis.org> - 2.3-1
- Updated to release 2.3.

* Sat Sep 22 2007 Dag Wieers <dag@wieers.com> - 2.1-1
- Updated to release 2.1.

* Sun Nov 27 2005 Dag Wieers <dag@wieers.com> - 2.0-1
- Initial package. (using DAR)
