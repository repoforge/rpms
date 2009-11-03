# $Id$

# Authority: dries
# Screenshot: http://www.nongnu.org/giftcurs/shots/giFTcurs-0.5.4.png
# ScreenshotURL: http://www.nongnu.org/giftcurs/shots.html

%define real_name giFTcurs

Summary: Console frontend to giFT.
Name: giftcurs
Version: 0.6.2
Release: 1.2%{?dist}
License: GPL
Group: Applications/Internet
URL: http://www.nongnu.org/giftcurs/

Source: http://savannah.nongnu.org/download/giftcurs/giFTcurs-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gift-devel, ncurses-devel, gettext, glib2-devel, bison

%description
giFTcurs is a cursed frontend to the giFT daemon and has been described as
“seriously slick”. It won’t work that well without giFT, which you should
have already.

%prep
%setup -n %{real_name}-%{version}

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{real_name}

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files -f %{real_name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO
%doc %{_mandir}/man?/giFTcurs*
%{_bindir}/giFTcurs

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.6.2-1.2
- Rebuild for Fedora Core 5.

* Thu Feb 03 2005 Dries Verachtert <dries@ulyssis.org> - 0.6.2-1
- Initial package.
