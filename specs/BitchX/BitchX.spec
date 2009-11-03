# $Id$
# Authority: matthias

Summary: Text mode IRC (Internet Relay Chat) client
Name: BitchX
Version: 1.1
Release: 1%{?dist}
Group: Applications/Internet
License: Distributable
URL: http://www.bitchx.org/
Source: http://bitchx.org/files/source/ircii-pana-%{version}-final.tar.gz
Patch0: ircii-pana-1.1-final-64bit.patch
Patch1: ircii-pana-1.1-final-fixes.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
#BuildRequires: gtk+-devel >= 1.2.8, imlib-devel, gnome-libs-devel
BuildRequires: openssl-devel, ncurses-devel

%description
BitchX is a text mode ircII client.  BitchX features include ANSI
color, easy to use shortcut commands, notify/protection/bot lists, 
mass commands and tools, an extended set of DCC commands and built-in 
CDCC, a link looker, extended scripting functionality, a screen client
which allows you to detach and reattach to an IRC session, and lots of 
help available online (many users, many available scripts and a
dedicated help channel--#BitchX on EFNET).


%prep
%setup -n BitchX 
%patch0 -p0 -b .64bit
%patch1 -p1 -b .fixes


%build
%configure \
    --enable-ipv6 \
    --with-ssl
### Include /usr/kerberos/include to accomodate RH9 and EL3
%{__make} %{?_smp_mflags} CFLAGS="%{optflags} -I/usr/kerberos/include"


%install
%{__rm} -rf %{buildroot} _doc
%makeinstall
# The BitchX -> BitchX-1.1-final symlink is useless for rpm installs, and it
# gets things wrong since it's absolute by default.
#{__rm} -f %{buildroot}%{_bindir}/BitchX
%{__mv} -f %{buildroot}%{_bindir}/BitchX-%{version}* \
           %{buildroot}%{_bindir}/BitchX
# Clean up docs in order to include them
%{__cp} -a doc _doc
%{__rm} -rf _doc/{BitchX.1,BitchX.bat.in,Makefile*,misc/,pana-docs/,README,README.OS2,win32/}


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-,root,root,0755)
%doc Changelog README* _doc/*
%{_bindir}/BitchX
%{_bindir}/scr-bx
%{_libdir}/bx/
%{_mandir}/man1/BitchX.1*


%changelog
* Tue Oct  3 2006 Matthias Saou <http://freshrpms.net/> 1.1-1
- Update to 1.1.
- Enable IPv6.
- Include 64bit patch and fixes from arved (FreeBSD) and Darwin ports.
- Disable gtk sub-package, if you want a GUI client, use X-Chat.
- Spec file cleanup.

* Thu Feb 15 2001 Tim Powers <timp@redhat.com>
- no longer obsoletes ircii

* Mon Feb  5 2001 Tim Powers <timp@redhat.com>
- include gtkBitchX for 7.x releases
- remove unneeded obsoletes

* Mon Jan 15 2001 Tim Powers <timp@redhat.com>
- excludearrch ia64

* Wed Dec 13 2000 Tim Powers <timp@redhat.com>
- patched with patch created by nimrood <nimrood@ONEBOX.COM> to fix
  the problem with malformed DNS answers
- patched so that the two things most people complain about are turned
  off by default, bold colons and the auto away message
- built for 6.x

* Mon Nov 20 2000 Tim Powers <timp@redhat.com>
- rebuilt to fix bad dir perms

* Wed Nov  1 2000 Tim Powers <timp@redhat.com>
- update to 1.0c17
- Invite patch no longer needed since it's fixed in the new
  sources, kept for reference

* Mon Jul 24 2000 Prospector <prospector@redhat.com>
- rebuilt

* Mon Jul 10 2000 Tim Powers <timp@redhat.com>
- rebuilt

* Wed Jul 05 2000 Tim Powers <timp@redhat.com>
- created new package, gtkBitchX for the gtk+ version
- built for 7.0

* Wed Jul 05 2000 Tim Powers <timp@redhat.com>
- updated to patch a problem where users were killing BitchX with invite
  commands
- built for 6.x

* Tue Dec 21 1999 Tim Powers <timp@redhat.com>
- rebuilt for 6.2

* Tue Jul 27 1999 Tim Powers <timp@redhat.com>
- updated to 75p3
- install manpage
- cleaned up spec file
- new patch for Makefile
- built for 6.1

* Wed Oct 06 1998 Michael Maher <mike@redhat.com>
- updated package
- changed spec file

* Fri May 15 1998 Michael Maher <mike@redhat.com>
- Built package
