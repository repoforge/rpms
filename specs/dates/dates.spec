# $Id$
# Authority: dag

%define desktop_vendor rpmforge

%define real_name Dates

Summary: Small, lightweight calendar
Name: dates
Version: 0.4.11
Release: 7%{?dist}
Group: Applications/Productivity
License: GPLv2+
URL: http://pimlico-project.org/dates.html

Source: http://ftp.gnome.org/pub/gnome/sources/dates/0.4/dates-%{version}.tar.bz2
Patch0: dates-0.4.11-fixdso.patch
Patch1: dates-0.4.11-ftbfs.patch
Patch2: dates-0.4.11-fixmake.patch

BuildRequires: desktop-file-utils
BuildRequires: evolution-data-server-devel
BuildRequires: gettext
BuildRequires: gtk2-devel
BuildRequires: intltool

%description
Dates is a small, lightweight calendar that uses Evolution Data Server as a
backend. Dates features an innovative, unified, zooming view and is designed
for use on primarily hand-held devices. It features both a â€˜vanillaâ€™ GTK
user interface and tailored support for the Nokia 770 maemo interface.

%prep
%setup
%patch0 -p1 -b .fixdso
%patch1 -p1 -b .ftbfs
%patch2 -p1 -b .fixmake

sed -i 's/SingleInstance/X-SingleInstance/' data/%{name}.desktop*

%build
%configure --disable-debug
%{__make} %{?_smp_mflags} 

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%find_lang Dates

desktop-file-install \
    --vendor %{desktop_vendor} \
    --delete-original  \
    --dir %{buildroot}%{_datadir}/applications     \
    %{buildroot}%{_datadir}/applications/%{name}.desktop


%clean
%{__rm} -rf %{buildroot}

%post
touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :
gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%files -f Dates.lang
%defattr(-, root, root, 0755)
%doc COPYING NEWS README
%doc %{_mandir}/man1/dates.1.gz
%{_bindir}/dates
%{_datadir}/applications/%{desktop_vendor}-dates.desktop
%{_datadir}/dates
%{_datadir}/icons/hicolor/*/apps/dates.*

%changelog
* Thu Nov 18 2010 Dag Wieers <dag@wieers.com> - 0.4.11-1
- Initial package. (using DAR)
