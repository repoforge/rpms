# $Id$
# Authority: dag

%define _libdir /%{_lib}

Summary: PAM module for auto blacklisting
Name: pam_abl
Version: 0.2.3
Release: 1%{?dist}
License: GPL
Group: System Environment/Base
URL: http://www.hexten.net/sw/pam_abl/

Source: http://dl.sf.net/sourceforge/pam-abl/pam_abl-%{version}.tar.gz	
Patch: pam_abl-0.2.3-fixes.patch
BuildRequires: pam-devel, db4-devel
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Provides auto blacklisting of hosts and users responsible for repeated failed
authentication attempts. Generally configured so that blacklisted users still
see normal login prompts but are guaranteed to fail to authenticate.

A command line tool allows to query or purge the databases used by the pam_abl
module.

%prep
%setup -n %{name}
%patch0 -p1

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 pam_abl.so %{buildroot}%{_libdir}/security/pam_abl.so
%{__install} -Dp -m0644 conf/pam_abl.conf %{buildroot}%{_sysconfdir}/security/pam_abl.conf
%{__install} -Dp -m0755 tools/pam_abl %{buildroot}%{_sbindir}/pam_abl
%{__install} -Dp -m0644 doc/pam_abl.1 %{buildroot}%{_mandir}/man1/pam_abl.1
%{__install} -d -m0755 %{buildroot}%{_localstatedir}/lib/abl/

### Clean up docdir
%{__rm} -rf doc/{CVS,._pam_abl.html,pam_abl.1}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS CONFIGURATION COPYING Copyright NEWS QUICKSTART THANKS
%doc conf/system-auth doc/
%doc %{_mandir}/man1/pam_abl.1*
%config(noreplace) %{_sysconfdir}/security/pam_abl.conf
%{_libdir}/security/pam_abl.so
%dir %{_localstatedir}/lib/abl/
%{_sbindir}/pam_abl

%changelog
* Mon Jan 15 2007 Dag Wieers <dag@wieers.com> - 0.2.3-1
- Initial package. (using DAR)
