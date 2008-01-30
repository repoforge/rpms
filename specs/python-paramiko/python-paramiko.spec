# $Id$
# Authority: dag

%define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")

%define real_name paramiko

Summary: SSH2 protocol for Python
Name: python-paramiko
Version: 1.7.2
Release: 1
License: GPL
Group: System Environment/Libraries
URL: http://www.lag.net/~robey/paramiko/

Source: http://www.lag.net/paramiko/download/paramiko-%{version}.zip
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: python-devel >= 2.2
Requires: python-crypto

Provides: paramiko
Obsoletes: paramiko <= %{version}-%{release}

%description
Paramiko is a module for python that implements the SSH2 protocol for secure
(encrypted and authenticated) connections to remote machines.  the module works
by taking a socket-like object that you pass in, negotiating with the remote
server, authenticating (using a password or a given private key), and opening
flow-controled "channels" to the server, which are returned as socket-like
objects. you are responsible for verifying that the server's host key is the
one you expected to see, and you have control over which kinds of encryption
or hashing you prefer (if you care), but all of the heavy lifting is done by
the paramiko module.

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
%doc LICENSE README docs/ tests/ demo*
%{python_sitelib}/paramiko/
%ghost %{python_sitelib}/paramiko/*.pyo

%changelog
* Tue Jan 22 2008 Dag Wieers <dag@wieers.com> - 1.7.2-1
- Updated to release 1.7.2.

* Mon Jun 11 2007 Dag Wieers <dag@wieers.com> - 1.7.1-1
- Updated to release 1.7.1.

* Mon Feb 19 2007 Dag Wieers <dag@wieers.com> - 1.7-1
- Updated to release 1.7.

* Mon Nov 20 2006 Dag Wieers <dag@wieers.com> - 1.6.4-1
- Updated to release 1.6.4.

* Wed Nov 01 2006 Dag Wieers <dag@wieers.com> - 1.6.3-2
- Added python-crypto dependency. (Will McDonald)

* Sun Oct 15 2006 Dag Wieers <dag@wieers.com> - 1.6.3-1
- Updated to release 1.6.3.

* Mon Oct 09 2006 Dag Wieers <dag@wieers.com> - 1.6.2-2
- Fixed group name.

* Thu Aug 17 2006 Dag Wieers <dag@wieers.com> - 1.6.2-1
- Updated to release 1.6.2.

* Mon Jul 10 2006 Dag Wieers <dag@wieers.com> - 1.6.1-1
- Updated to release 1.6.1.

* Fri May 12 2006 Dag Wieers <dag@wieers.com> - 1.6-1
- Updated to release 1.6.

* Fri Mar 10 2006 Dag Wieers <dag@wieers.com> - 1.5.3-2
- Added .pyo ghost files.

* Mon Feb 20 2006 Dag Wieers <dag@wieers.com> - 1.5.3-1
- Updated to release 1.5.3.

* Wed Jan 11 2006 Dag Wieers <dag@wieers.com> - 1.5.2-1
- Initial package. (using DAR)
