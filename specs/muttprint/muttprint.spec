# $Id: muttprint.spec 171 2004-04-05 04:43:07Z bert $
#
# Authority: bert
#
# Upstream: <Bernhard.Walle@gmx.de>
#

Name: muttprint
Version: 0.72
Release: 1	
License: GPL
Group: Applications/Mail
Source: muttprint-%{version}.tar.gz
BuildArch: noarch
URL: http://muttprint.sourceforge.net/
Packager: Bert de Bruijn <bert@debruijn.be)
Requires: tetex >= 1.0 psutils perl
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Prefix: %{_prefix}
Summary: pretty printing of mails with Mutt

%description
Muttprint is a utility that formats the printing of Mutt and other mail clients
like XFMail or PINE to be like the printing of Netscape Messenger or Kmail. It
can print a little penguin on the first page and a headline on every page.
Furthermore, it only prints the most important headers, but not the whole
plethora of them.

%build
make

%prep
%setup

%install

rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{name}/translations
mkdir -p $RPM_BUILD_ROOT/%{_mandir}/man1
mkdir -p $RPM_BUILD_ROOT/%{_mandir}/{de,es,it}/man1
mkdir -p $RPM_BUILD_ROOT/%{_docdir}

make prefix=$RPM_BUILD_ROOT/%{prefix} mandir=$RPM_BUILD_ROOT/%{_mandir} \
		docdir=$RPM_BUILD_ROOT/%{_docdir} install

%clean 
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-, root, root, 0755)
%{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man1/muttprint.1.gz
%{_mandir}/*/man1/muttprint.1.gz
%{_docdir}/*


%changelog
* Tue Apr 06 2004 Bert de Bruijn <bert@debruijn.be>
- minor fixes for inclusion in rpm repository
* Mon Jul 28 2003 Bernhard Walle <Bernhard.Walle@gmx.de>
- added rule to build muttprint-langinfo
* Mon Apr 14 2003 Bernhard Walle <Bernhard.walle@gmx.de>
- changed translation place to /prefix/share/muttprint/translations
* Mon Apr 07 2003 Bernhard Walle <Bernhard.walle@gmx.de>
- changed translation place to /prefix/lib/muttprint/translations
* Thu Feb 20 2003 Bernhard Walle <Bernhard.Walle@gmx.de>
- changed translation place to /prefix/share/muttprint/translations
* Sat Dec 15 2001 Bernhard Walle <Bernhard.Walle@gmx.de>
- new version
* Fri Oct 05 2001 Bernhard Walle <Bernhard.Walle@gmx.de>
- new version
- new URL: http://muttprint.sourceforge.net
- new directory: /prefix/lib/muttprint for translation file
  (in earlier versions the translation were included in the
  muttprint-executable)
* Sun Aug 05 2001 Bernhard Walle <Bernhard.Walle@gmx.de>
- new version
- changed specfile because of writing a Makefile
- new Spanish description
- new Italian description
* Sat Jul 07 2001 Bernhard Walle <Bernhard.Walle@gmx.de>
- new version
* Sun Jul 01 2001 Bernhard Walle <Bernhard.Walle@gmx.de>
- new version => changed dependencies
* Fri Jun 22 2001 Bernhard Walle <Bernhard.Walle@gmx.de>
- new version
* Sat May 12 2001 Bernhard Walle <Bernhard.Walle@gmx.de>
- first release with changelog

# vim: sw=8 ts=8
