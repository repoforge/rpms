# $Id$
# Authority: dag

# ExclusiveDist: el2 el3 el4 el5

Summary: Point-to-Point Tunneling Protocol (PPTP) Client
Name: pptp
Version: 1.7.2
Release: 8.1%{?dist}
License: GPLv2+
Group: Applications/Internet
URL: http://pptpclient.sourceforge.net/

Source0: http://downloads.sf.net/pptpclient/pptp-%{version}.tar.gz
Patch0: pptp-1.7.2-compat.patch
Patch1: pptp-1.7.2-ip-path.patch
Patch2: pptp-1.7.2-pptpsetup.patch
Patch3: pptp-1.7.2-makedeps.patch
Patch4: pptp-1.7.2-pptpsetup-encrypt.patch
Patch5: pptp-1.7.2-pptpsetup-mppe.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires: ppp >= 2.4.2
Requires: /sbin/ip

%description
Client for the proprietary Microsoft Point-to-Point Tunneling
Protocol, PPTP. Allows connection to a PPTP based VPN as used
by employers and some cable and ADSL service providers.

%package setup
Summary: PPTP Tunnel Configuration Script
Group: Applications/Internet
Requires: %{name} = %{version}-%{release}

%description setup
This package provides a simple configuration script for setting up PPTP
tunnels.

%prep
%setup

# Remove reference to stropts.h, not shipped in F9 onwards (applied upstream)
%patch0 -p0 -b .compat

# Make location of "ip" binary build-time configurable (applied upstream)
%patch1 -p0 -b .ip-path

# Retain permissions on /etc/ppp/chap-secrets (#492090, applied upstream)
%patch2 -p0 -b .bz492090

# Fix Makefile dependencies to support parallel make (applied upstream)
%patch3 -p0 -b .makedeps

# Don't check for MPPE capability in kernel or pppd unless we're creating a
# tunnel that requires encryption (applied upstream)
%patch4 -p0 -b .encrypt

# Don't check for MPPE capability in kernel and pppd at all because current
# Fedora releases and EL >= 5 include MPPE support out of the box (#502967)
%patch5 -p1 -b .mppe

# Pacify rpmlint
%{__perl} -pi -e 's/install -o root -m 555 pptp/install -m0755 pptp/;' Makefile

%build
%{__make} %{?_smp_mflags} CFLAGS="-Wall %{optflags}" IP=/sbin/ip

%install
%{__rm} -rf %{buildroot}
%{__make} DESTDIR=%{buildroot} install

%{__install} -d -m0750 %{buildroot}%{_localstatedir}/run/pptp/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING DEVELOPERS NEWS README TODO USING
%doc ChangeLog Documentation/DESIGN.PPTP PROTOCOL-SECURITY
%doc %{_mandir}/man8/pptp.8*
# /etc/ppp is hardcoded instead of using %{_sysconfdir}/ppp because the
# Fedora ppp package hardcodes the directory name
%config(noreplace) /etc/ppp/options.pptp
%{_sbindir}/pptp
%dir %attr(750, root, root) %{_localstatedir}/run/pptp/

%files setup
%defattr(-, root, root, 0755)
%doc %{_mandir}/man8/pptpsetup.8*
%{_sbindir}/pptpsetup

%changelog
* Mon Jan 24 2011 Dag Wieers <dag@wieers.com> - 1.7.2-8.1
- Imported from RHEL 5.

* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 1.7.2-8.1
- Rebuilt for RHEL 6

* Thu Sep 24 2009 Paul Howarth <paul@city-fan.org> 1.7.2-8
- Split pptpsetup into subpackage to avoid perl dependency (#524972)

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jun  1 2009 Paul Howarth <paul@city-fan.org> 1.7.2-6
- Don't check for MPPE capability in kernel and pppd unless we're creating a
  tunnel that requires encryption
- Don't check for MPPE capability in kernel and pppd at all because current
  Fedora releases and EL >= 5 include MPPE support out of the box (#502967)

* Wed Mar 25 2009 Paul Howarth <paul@city-fan.org> 1.7.2-5
- Retain permissions on /etc/ppp/chap-secrets when using pptpsetup (#492090)
- Use upstream versions of patches
- Re-enable parallel build; Makefile dependencies now fixed
- Use perl rather than sed to edit Makefile, for spec compatibility with
  ancient distro releases

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon May 19 2008 Paul Howarth <paul@city-fan.org> 1.7.2-3
- Add dependency on /sbin/ip
- Disable parallel make - object files are missing dependency on config.h

* Mon May 19 2008 Paul Howarth <paul@city-fan.org> 1.7.2-2
- Use /sbin/ip, not /bin/ip for routing

* Wed May 14 2008 Paul Howarth <paul@city-fan.org> 1.7.2-1
- Update to 1.7.2
- New script and manpage: pptpsetup
- Add patch to remove reference to stropts.h, not shipped in F9 onwards

* Wed Feb 13 2008 Paul Howarth <paul@city-fan.org> 1.7.1-4
- Rebuild with gcc 4.3.0 for Fedora 9

* Fri Aug 24 2007 Paul Howarth <paul@city-fan.org> 1.7.1-3
- Change download URL from df.sf.net to downloads.sf.net
- Expand tabs in spec
- Clarify license as GPL version 2 or later

* Wed Aug 30 2006 Paul Howarth <paul@city-fan.org> 1.7.1-2
- FE6 mass rebuild

* Mon Feb 13 2006 Paul Howarth <paul@city-fan.org> 1.7.1-1
- new upstream version 1.7.1 (fixes #166394)
- include new document PROTOCOL-SECURITY
- cosmetic change: replace variables with macros

* Wed Aug 10 2005 Paul Howarth <paul@city-fan.org> 1.7.0-2
- own directory %%{_localstatedir}/run/pptp

* Thu Jul 28 2005 Paul Howarth <paul@city-fan.org> 1.7.0-1
- new upstream version 1.7.0
- remove patch, included upstream
- edit Makefile to prevent attempted chown in %%install
- remove redundant %%attr tag in %%files
- honour $RPM_OPT_FLAGS
- ensure directories have correct permissions

* Fri May 27 2005 Paul Howarth <paul@city-fan.org> 1.6.0-5
- bump and rebuild

* Tue May 17 2005 Paul Howarth <paul@city-fan.org> 1.6.0-4
- rebuild with dist tags

* Tue May 10 2005 Paul Howarth <paul@city-fan.org> 1.6.0-3
- fix URL for SOURCE0 not to point to a specific sf.net mirror

* Tue May 10 2005 Paul Howarth <paul@city-fan.org> 1.6.0-2
- Weed out documentation useful only to developers
- Add dist tag
- Use full URL for SOURCE0
- Fix permissions on %%{_sbindir}/pptp

* Fri May  6 2005 Paul Howarth <paul@city-fan.org> 1.6.0-1
- First build for Fedora Extras, based on upstream spec file
