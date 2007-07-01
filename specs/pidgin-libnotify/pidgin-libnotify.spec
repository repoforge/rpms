# $Id$
# Authority: hadams

%global	pidgin_version 2.0.0

Name:		pidgin-libnotify
Version:	0.13
Release:	1
Summary:	Libnotify Pidgin plugin 

Group:		Applications/Internet
License:	GPL
URL:		http://gaim-libnotify.sourceforge.net/

Source0:	http://downloads.sourceforge.net/gaim-libnotify/pidgin-libnotify-%{version}.tar.gz
#Patch0:		%{name}-renamed-to-pidgin.patch

BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:	libnotify-devel >= 0.3.2
BuildRequires:	gtk2-devel
BuildRequires:	pidgin-devel >= %{pidgin_version}
BuildRequires:	libtool
BuildRequires:	gettext

Requires:	pidgin >= %{pidgin_version}

## Provides a proper upgrade path from gaim-libnotify installations.
Provides:	gaim-libnotify = %{version}-%{release} 
Obsoletes:	gaim-libnotify < %{version}-%{release}

%description
This is a plugin for the open-source Pidgin instant messaging client that uses
libnotify to display graphic notifications of new messages and other events
such as a buddy signing on or off.


%prep
%setup -q -n "pidgin-libnotify-%{version}"
#%patch -p0 -b .renamed-to-pidgin
autoreconf


%build
%configure --disable-static
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
%find_lang pidgin-libnotify


%clean
rm -rf %{buildroot}


%files -f pidgin-libnotify.lang
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING NEWS TODO
%exclude %{_libdir}/purple-2/*.la
%{_libdir}/purple-2/pidgin-libnotify.so


%changelog
* Tue Jul 01 2007 Heiko Adams <info@fedora-blog.de> - 0.13-1
- Updated to 0.13 and rebuild for CentOS

* Tue May 29 2007 Stu Tomlinson <stu@nosnilmot.com> - 0.12-7.1
- Add gtk2-devel BuildRequires to work around missing requires in
  libnotify-devel in FC6

* Fri May 18 2007 Peter Gordon <peter@thecodergeek.com> - 0.12-7
- Make Provides/Obsoletes tags use macros for the Version/Release of the
  upgrade.

* Fri May 18 2007 Peter Gordon <peter@thecodergeek.com> - 0.12-6
- Package renamed to pidgin-libnotify.
- Reword earlier %%changelog entry.

* Fri May 18 2007 Warren Togami <wtogami@redhat.com> - 0.12-5
- buildreq gettext (#240604)

* Sat May 12 2007 Peter Gordon <peter@thecodergeek.com> - 0.12-4
- Gaim has been renamed to Pidgin: adjust the sources accordingly.  
- Add patch based on the Arch Linux packaging to make the sources and build
  scripts properly use the new Pidgin/Libpurple nomenclature of what was
  formerly called Gaim.
  + renamed-to-pidgin.patch
- Drop gtk2-devel build dependency (pulled in by libnotify-devel).
- Update Source0 to point to simpler SourceForge URL.

* Sun Dec 10 2006 Peter Gordon <peter@thecodergeek.com> - 0.12-3
- Bump EVR to fix CVS tagging issue

* Sun Dec 10 2006 Peter Gordon <peter@thecodergeek.com> - 0.12-2
- Shorten line lengths in %%description (and rewrite it a bit)
- Add gaim runtime requirement so that the parent directory of the plugin in
  %%{_libdir}/gaim is properly owned
- Removed unnecessary perl(XML::Parser) and gettext BuildRequires
- Add TODO to %%doc

* Sat Dec 09 2006 Peter Gordon <peter@thecodergeek.com> - 0.12-1
- Initial packaging for Fedora Extras
