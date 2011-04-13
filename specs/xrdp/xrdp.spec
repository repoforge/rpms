# $Id$
# Authority: dag

Summary: Open source remote desktop protocol (RDP) server
Name: xrdp
Version: 0.4.0
Release: 1%{?dist}
License: GPL
Group: User Interface/X
URL: http://xrdp.sourceforge.net/

Source: http://dl.sf.net/xrdp/xrdp-%{version}.tar.gz
Patch0: xrdp-0.4.0-sesman.patch
Patch1: xrdp-0.4.0-sesmantools.patch
Patch2: xrdp-0.4.0-docs.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

#BuildRequires: libnss-mysql
#BuildRequires: libpam-devel
#BuildRequires: libssl-devel

%description
The goal of this project is to provide a fully functional Linux terminal
server, capable of accepting connections from rdesktop and Microsoft's
own terminal server / remote desktop clients.

%prep
%setup
%patch0
%patch1
%patch2

%{__perl} -pi.orig -e 's|/lib\b|/%{_lib}|g' Makefile */Makefile

%build
#configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} installdeb DESTDIRDEB="%{buildroot}"
%{__install} -Dp -m0755 sesman/libscp/libscp.so %{buildroot}%{_libdir}/xrdp/libscp.so

### Clean up buildroot
%{__rm} -rf %{buildroot}%{_sysconfdir}/init.d/xrdp_control.sh

%clean
%{__rm} -rf %{buildroot}

%files
%doc COPYING *.txt instfiles/*.sh
%doc %{_mandir}/man5/*.5*
%doc %{_mandir}/man8/*.8*
%config(noreplace) %{_sysconfdir}/xrdp/
%config(noreplace) %{_sysconfdir}/pam.d/sesman
%{_libdir}/xrdp/

%changelog
* Wed Sep 12 2007 Dag Wieers <dag@wieers.com> - 0.4.0-1
- Initial package. (using DAR)
