# $Id$
# Authority: dries
# Upstream: Stonki <stonki$stonki,de>

Summary: Barcode and label printing application
Name: kbarcode
Version: 2.0.5
Release: 1
License: GPL
Group: Applications/Publishing
URL: http://www.kbarcode.net/

Source: http://dl.sf.net/kbarcode/kbarcode-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++, kdelibs-devel, gettext, barcode-devel
BuildRequires: pcre-devel

%description
KBarcode is a barcode and label printing application for KDE 3. It can
be used to print everything from simple business cards up to complex
labels with several barcodes, such as article descriptions. KBarcode
comes with an easy-to-use WYSIWYG label designer, a setup wizard,
batch import of labels (directly from the delivery note), thousands
of predefined labels, database managment tools, and translations in
many languages. Even printing more than 10,000 labels in one go is no
problem for KBarcode. Additionally, it is a simple xbarcode
replacement for the creation of barcodes. All major types of barcodes
like EAN, UPC, CODE39, and ISBN are supported.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO
%{_libdir}/kde3/kfile_kbarcode.*
%{_datadir}/services/kfile_kbarcode.desktop
%{_datadir}/apps/kbarcode/
%{_datadir}/applications/kde/kbarcode*.desktop
%{_datadir}/icons/*/*/*/*barcode*.png
%{_bindir}/kbarcode

%changelog
* Sun Nov 12 2006 Dries Verachtert <dries@ulyssis.org> - 2.0.5-1
- Updated to release 2.0.5.

* Mon Aug 07 2006 Dries Verachtert <dries@ulyssis.org> - 2.0.4-1
- Updated to release 2.0.4.

* Thu Apr 27 2006 Dries Verachtert <dries@ulyssis.org> - 2.0.2-1
- Updated to release 2.0.2.

* Thu Mar 16 2006 Dries Verachtert <dries@ulyssis.org> - 2.0.0-1
- Updated to release 2.0.0.

* Wed Jan 11 2006 Dries Verachtert <dries@ulyssis.org> - 1.9.10-1
- Initial package.
