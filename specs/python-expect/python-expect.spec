# $Id$
# Authority: dag
# Upstream: <noah$noah,org>

%define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")
%define python_version %(python2 -c 'import sys; print sys.version[:3]')

%define real_name pexpect

Summary: Expect module for Python
Name: python-expect
Version: 0.99999b
Release: 2.2%{?dist}
License: PSFL
Group: Development/Languages
URL: http://pexpect.sourceforge.net/

Source: http://dl.sf.net/pexpect/pexpect-%{version}.tgz
Source1: http://dl.sf.net/pexpect/pexpect-doc.tgz
Source2: http://dl.sf.net/pexpect/pexpect-examples.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Obsoletes: pexpect <= %{version}-%{release}
Obsoletes: python-pexpect <= %{version}-%{release}
BuildRequires: python-devel >= 2.2
Requires: python >= %{python_version}

%description
Pexpect is a pure Python module for spawning child applications; controlling
them; and responding to expected patterns in their output. Pexpect works like
Don Libes' Expect. Pexpect allows your script to spawn a child application and
control it as if a human were typing commands.

Pexpect can be used for automating interactive applications such as ssh, ftp,
passwd, telnet, etc. It can be used to a automate setup scripts for
duplicating software package installations on different servers. It can be
used for automated software testing. Pexpect is in the spirit of Don Libes'
Expect, but Pexpect is pure Python. Unlike other Expect-like modules for
Python, Pexpect does not require TCL or Expect nor does it require C
extensions to be compiled. It should work on any platform that supports the
standard Python pty module.

%prep
%setup -n %{real_name}-%{version} -a1 -a2

%build
%{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root="%{buildroot}" --prefix="%{_prefix}"

### Needed for chess example
%{__mv} -f ANSI.py screen.py FSM.py examples/

### Clean up buildroot
%{__rm} -rf doc/CVS/ examples/CVS/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README.txt doc/ examples/
%{python_sitelib}/pexpect.py
%{python_sitelib}/pexpect.pyc
%ghost %{python_sitelib}/pexpect.pyo

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.99999b-2.2
- Rebuild for Fedora Core 5.

* Mon Sep 12 2005 Dag Wieers <dag@wieers.com> - 0.99999b-2
- Added python-pexpect as obsoletes.

* Mon Sep 12 2005 Dag Wieers <dag@wieers.com> - 0.99999b-1
- Initial package. (using DAR)
