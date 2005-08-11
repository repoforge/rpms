# $Id$
# Authority: dag

Summary: Lightweight multi-tabbed X terminal
Name: mrxvt
Version: 0.4.1
Release: 1
License: GPL
Group: User Interface/X
URL: http://materm.sourceforge.net/

Source: http://dl.sf.net/materm/mrxvt-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: XFree86-devel, freetype-devel
#Requires:  qt >= 2.3.0
Obsoletes: materm

%description
Mrxvt (previously named as materm) is a lightweight and powerful
multi-tabbed X terminal emulator based on the popular rxvt and aterm.
It implements many useful features seen in some modern X terminal
emulators, like gnome-terminal and konsole, but keep to be lightweight
and independent from the GNOME and KDE desktop environment.

%prep
%setup

%build
%configure --enable-everything
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING CREDITS FAQ NEWS TODO doc/README* doc/TIPS
%doc doc/menu/ doc/mrxvt.vbs doc/mrxvtset.pl doc/xterm.seq doc/*.txt
%doc %{_mandir}/man1/mrxvt.1*
%{_bindir}/mrxvt
%{_datadir}/pixmaps/mrxvt*.png
%{_datadir}/pixmaps/mrxvt*.xpm
%exclude %{_docdir}/mrxvt/

%changelog
* Thu Aug 11 2005 Dag Wieers <dag@wieers.com> - 0.4.1-1
- Initial package. (using DAR)
