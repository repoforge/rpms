# $Id$
# Authority: dries

%define real_name kmymoney2

Summary: Double-entry accounting software package
Name: kmymoney
Version: 0.6
Release: 1
License: GPL
Group: Applications/Productivity
URL: http://kmymoney2.sourceforge.net/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://dl.sf.net/kmymoney2/kmymoney2-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc, make, libpng-devel, libart_lgpl-devel
BuildRequires: arts-devel, gcc-c++, gettext, XFree86-devel
BuildRequires: zlib-devel, qt-devel, libjpeg-devel, kdelibs-devel
%{?fc2:BuildRequires: libselinux-devel}

%description
KMyMoney is striving to be a full-featured replacement for your
Windows-based finance software. We are a full double-entry accounting
software package, for personal or small-business use.

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
%doc BUGS TODO ChangeLog.original README AUTHORS INSTALL ChangeLog COPYING
%doc %{_datadir}/doc/HTML/en/kmymoney2
%doc %{_mandir}/man?/*
%{_datadir}/apps/kmymoney2
%{_datadir}/applnk/Applications/kmymoney2.desktop
%{_datadir}/icons/*/*/apps/kmymoney2.png
%{_datadir}/icons/*/*/mimetypes/kmy.png
%{_datadir}/mimelnk/application/x-kmymoney2.desktop
%{_bindir}/*

%changelog
* Sun Jun 20 2004 Dries Verachtert <dries@ulyssis.org> - 0.6-1
- Initial package.
