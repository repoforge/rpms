# $Id$
# Authority: bert
# Upstream: <Bernhard,Walle$gmx,de>

Summary: Pretty printing of mails with Mutt
Name: muttprint
Version: 0.72d
Release: 1%{?dist}
License: GPL
Group: Applications/Internet
URL: http://muttprint.sourceforge.net/

Source: http://dl.sf.net/muttprint/muttprint-%{version}.tar.gz
Patch0: muttprint-0.72d-css.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
Requires: tetex >= 1.0, psutils, perl

%description
Muttprint is a utility that formats the printing of Mutt and other mail clients
like XFMail or PINE to be like the printing of Netscape Messenger or Kmail. It
can print a little penguin on the first page and a headline on every page.
Furthermore, it only prints the most important headers, but not the whole
plethora of them.

%prep
%setup
%patch0

%build
%{__make} clean -C langinfo
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
#%{__install} -d -m0755 doc-rpm/

%{__make} install prefix="%{buildroot}%{_prefix}" \
	mandir="%{buildroot}%{_mandir}" \
	docdir="$(pwd)/doc-rpm"

### Clean up buildroot
%{__rm} -rf %{buildroot}%{_docdir}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc doc-rpm/muttprint/*
%doc %{_mandir}/man1/muttprint.1*
%doc %{_mandir}/*/man1/muttprint.1*
%{_bindir}/muttprint
%exclude %{_bindir}/muttprint-langinfo
%{_datadir}/muttprint/

%changelog
* Fri May 04 2007 Dag Wieers <dag@wieers.com> - 0.72d-1
- Updated to release 0.72d.

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
