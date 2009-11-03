# $Id$
# Authority: dag

%define _libdir /%{_lib}

Summary: PAM module for use with SSH keys and ssh-agent
Name: pam_ssh
Version: 1.91
Release: 1%{?dist}
License: BSD
Group: System Environment/Base
URL: http://sourceforge.net/projects/pam-ssh/

Source: http://dl.sf.net/sourceforge/pam-ssh/pam_ssh-%{version}.tar.bz2
Patch0: pam_ssh-1.91-getpwnam.patch
Patch1: pam_ssh-1.91-var_run.patch
Patch2: pam_ssh-1.91-man_agent_files.diff
Patch3: pam_ssh-1.91-include_md5.diff
Patch4: pam_ssh-1.91-include_syslog.diff
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Requires: openssh-clients
BuildRequires: pam-devel, openssh-clients, openssl-devel

%description
This PAM module provides single sign-on behavior for UNIX using SSH keys. 
Users are authenticated by decrypting their SSH private keys with the 
password provided. In the first PAM login session phase, an ssh-agent 
process is started and keys are added. The same agent is used for the
following PAM sessions. In any case the appropriate environment variables
are set in the session phase.

%prep
%setup
%patch0 -p1
%patch1 -p1
%patch2 -p0
%patch3 -p1
%patch4 -p1

%build
%configure  --with-pam-dir="%{_libdir}/security/"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%{__install} -d -m0755 %{buildroot}%{_localstatedir}/run/pam_ssh/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%doc %{_mandir}/man8/pam_ssh.8*
%exclude %{_libdir}/security/pam_ssh.la
%{_libdir}/security/pam_ssh.so
%dir %{_localstatedir}/run/pam_ssh/

%changelog
* Mon Jan 15 2007 Dag Wieers <dag@wieers.com> - 1.91-1
- Initial package. (using DAR)
