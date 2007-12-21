# $Id$

# Authority: dag

Summary: Text-mode player for CDs and MP3 files
Name: orpheus
Version: 1.2
Release: 0.2
License: GPL
Group: Applications/Multimedia
URL: http://konst.org.ua/orpheus/

Source: http://thekonst.net/download/orpheus-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: ncurses-devel

%description
Orpheus is a text-mode player for CDs and files of MP3 format. It can
retrieve CDDB information for compact-discs, and save and load
playlists. Nice interface to modify MP3 ID tags is provided.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc ChangeLog COPYING README TODO
%{_bindir}/*

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.2-0.2
- Rebuild for Fedora Core 5.

* Mon Jul 28 2003 Dag Wieers <dag@wieers.com> - 1.2-0
- Initial package. (using DAR)
