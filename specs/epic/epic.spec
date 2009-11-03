# $Id$
# Authority: dag
# Upstream: <list$epicsol,org>

Summary: IrcII chat client
Name: epic
Version: 2.2
Release: 1%{?dist}
Epoch: 4
License: Distributable
Group: Applications/Communications
URL: http://www.epicsol.org/

Source0: ftp://ftp.epicsol.org/pub/epic/EPIC4-PRODUCTION/epic4-%{version}.tar.bz2
Source1: ftp://ftp.epicsol.org/pub/epic/EPIC4-PRODUCTION/epic4-help-current.tar.gz
Source2: epic.wmconfig
Source3: ircII.servers
Source4: http://dl.sf.net/splitfire/sf-1.35.irc.gz
Source5: http://splitfire.sourceforge.net/schemes/sf-bitchx-scheme.irc.gz
Source6: http://splitfire.sourceforge.net/schemes/sf-eggsandham-scheme.irc.gz
Source7: http://splitfire.sourceforge.net/schemes/sf-light-scheme.irc.gz
Source8: http://splitfire.sourceforge.net/schemes/sf-perry-scheme.irc.gz
Patch0: toggle-stop-screen-patch
Patch1: epic-default.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
EPIC (Enhanced Programmable ircII Client) is an advanced ircII chat
client.  Chat clients connect to servers around the world, enabling
you to chat with other people.

%prep
%setup -n epic4-%{version} -a 1
#%patch -p1 -b .stop
#%patch1 -p0 -b .default

### Clean up CVS dirs
find . -type d -name CVS -exec %{__rm} -rf {} \; || :

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install installhelp \
	CFLAGS="%{optflags}" \
	IP="%{buildroot}" \
	prefix="%{_prefix}" \
	mandir="%{_mandir}"

%{__ln_s} -f epic-EPIC4-%{version} %{buildroot}%{_bindir}/epic

for file in %{SOURCE4} %{SOURCE5} %{SOURCE6} %{SOURCE7} %{SOURCE8}; do
	sNAME="${file//%.gz/}"
	bNAME="$(basename $sNAME)"
	zcat $file | sed -e 's|^\(\^set HELP_PATH.*\)|#\1|' >$bNAME;
	%{__install} -p -m0644 $bNAME %{buildroot}%{_datadir}/epic/script/
done;

%{__install} -p %{SOURCE3} %{buildroot}%{_datadir}/epic/

### Clean up Makefiles
find %{buildroot} -type f -name Makefile -exec %{__rm} -f {} \; || :

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc BUG_FORM COPYRIGHT INSTALL KNOWNBUGS README UPDATES doc/*
%doc %{_mandir}/man?/*
%dir %{_datadir}/epic/
%config(noreplace) %{_datadir}/epic/ircII.servers
%{_bindir}/*
%{_datadir}/epic/help/
%{_datadir}/epic/script/
%exclude %{_libexecdir}/wserv4

%changelog
* Sat Mar 19 2005 Bert de Bruijn <bert@debruijn.be> - 4:2.2-1
- Updated to release 2.2.

* Thu Jul 15 2004 Bert de Bruijn <bert@debruijn.be> - 4:2.0-1
- Updated to release 2.0.

* Sat Apr 17 2004 Dag Wieers <dag@wieers.com> - 4:1.0.1-16
- Clean up SPEC file.

* Tue Nov 11 2003 Jeremy Katz <katzj@redhat.com> 4:1.0.1-16
- add patch for buffer overflow (CAN-2003-0328) from
  ftp://ftp.prbh.org/pub/epic/patches/alloca_underrun-patch-1

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Jun  3 2003 Jeremy Katz <katzj@redhat.com> 4:1.0.1-14
- generated files to generate files.  fix gcc 3.3 build for real

* Thu May 22 2003 Jeremy Katz <katzj@redhat.com> 4:1.0.1-13
- fix build with gcc 3.3

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Wed Dec 25 2002 Tim Powers <timp@redhat.com> 4:1.0.1-11
- fix references to %%install in the changelog so that it will build

* Sun Dec  1 2002 Jeremy Katz <katzj@redhat.com> 1.0.1-10
- own %%{_datadir}/epic/help (#74031)

* Tue Oct 29 2002 Jeremy Katz <katzj@redhat.com> 1.0.1-9
- rebuild on all arches

* Fri Jun 21 2002 Tim Powers <timp@redhat.com> 1.0.1-8
- automated rebuild

* Mon Jun  3 2002 Jeremy Katz <katzj@redhat.com> 1.0.1-7
- include more of the docs
- patch the default global to enable 8-bit chars by default (#65033)

* Thu May 23 2002 Tim Powers <timp@redhat.com> 1.0.1-6
- automated rebuild

* Fri May 10 2002 Jeremy Katz <katzj@redhat.com> 1.0.1-5
- rebuild in new environment

* Wed Feb 27 2002 Jeremy Katz <katzj@redhat.com> 1.0.1-4
- rebuild
- desktop entries for console apps are silly, kill it

* Wed Jan 09 2002 Tim Powers <timp@redhat.com> 1.0.1-3
- automated rebuild

* Wed Jan  2 2002 Jeremy Katz <katzj@redhat.com> 1.0.1-2
- rebuild in new environment
- fix desktop file

* Tue Oct 30 2001 Crutcher Dunnavant <crutcher@redhat.com> 1.0.1-1
- iterate to newest version

* Thu Feb 15 2001 Tim Powers <timp@redhat.com>
- no longer conflicts with ircii

* Mon Jul 24 2000 Prospector <prospector@redhat.com>
- rebuilt

* Mon Jul 10 2000 Tim Powers <timp@redhat.com>
- rebuilt

* Tue Jun 6 2000 Tim Powers <timp@redhat.com>
- fix man page location
- use %%configure and %%makeinstall
- use predefined RPM macros wherever possible
- use applnk instead of wmconfig
- include the stuff in %%{_libexecdir}

* Tue May 9 2000 Tim Powers <timp@redhat.com>
- built for 7.0

* Sun Jan  9 2000 Matt Wilson <msw@redhat.com>
- updated to epic4-2000
- updated to splitfire v1.30a

* Tue Nov 9 1999 Tim Powers <timp@redhat.com>
- updated to 4pre2.003 , two of the patches no longer needed, so they're
	dropped
- patched so that epic no longer looks for help files in /usr/lib/irc, instead
	looks in the correct place, /usr/share/epic/help

* Tue Jul 13 1999 Tim Powers <timp@redhat.com>
- rebuilt for 6.1

* Tue Apr 13 1999 Michael Maher <mike@redhat.com>
- built package for 6.0

* Wed Oct 22 1998 <msw@redhat.com>
- Copy the splitfire script into the right directory
- Fixed diretory attributes.

* Wed Oct 21 1998 <msw@redhat.com>
- Rebuilt, moved help into main package.

* Thu Aug 18 1998 Manoj Kasichainula <manojk+rpm@io.com>
- Updated prog and help to 4pre2
- renamed to epic, since the web page doesn't call it ircii-epic.
- Use %defattr
- Changed server list, since current one seems out of date
- Other minor changes

* Sun May 17 1998 Manoj Kasichainula <manojk+rpm@io.com>
- Added help package (though a bit out of date)
- Uses bz2 file (needs bzip2 now)
- Minor spec file changes

* Sat May  9 1998 Anders Andersson <anders@sanyusan.se>
- Upgraded to pre1.200

* Tue Apr 28 1998 Maciej Lesniewski <nimir@kis.p.lodz.pl>
- Upgraded to pre1.100
- Build for RH5
- Complex changes of %%install

* Sat Mar 28 1998 Maciej Lesniewski <nimir@kis.p.lodz.pl>
- Upgraded to pre1.049

* Sat Mar 21 1998 Maciej Lesniewski <nimir@kis.p.lodz.pl>
- Initial release (pre1.047)
- Small patch to disable loading local-script in global file
