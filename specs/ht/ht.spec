# $Id: $

# Authority: dries

Summary: File editor, viewer and analyzer for text, binary and especially executables
Name: ht
Version: 0.7.5
Release: 1
License: GPL
Group: Applications/Editors
URL: http://hte.sourceforge.net/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://dl.sf.net/hte/ht-%{version}.tar.bz2
BuildRoot: %{_tmppath}/root-%{name}-%{version}
BuildRequires: ncurses-devel

# Screenshot: http://hte.sourceforge.net/screenshots/screenshot5.gif
# ScreenshotURL: http://hte.sourceforge.net/screenshots.htm

%description
The HT editor is a file editor, viewer and analyzer for text, binary and
especially executables. It has support for the following formats: common
object file format (COFF), executable and linkable format (ELF), linear
executables (LE), standard dos executables (MZ), new executables (NE),
portable executables (PE32, PE64), java class files (CLASS).

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING KNOWNBUGS NEWS README TODO
%{_bindir}/ht

%changelog
* Sat Mar 20 2004 Dries Verachtert <dries@ulyssis.org> 0.7.5-1
- Initial package
