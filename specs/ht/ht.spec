# $Id$
# Authority: dries
# Upstream: Stefan Weyergraf <sw$weyergraf,de>
# Upstream: Sebastian Biallas <sb$biallas,net>
# Screenshot: http://hte.sourceforge.net/screenshots/screenshot5.gif
# ScreenshotURL: http://hte.sourceforge.net/screenshots.htm

Summary: File editor, viewer and analyzer for text, binary and executables
Name: ht
Version: 0.8.0
Release: 1.2%{?dist}
License: GPL
Group: Applications/Editors
URL: http://hte.sourceforge.net/

Source: http://dl.sf.net/hte/ht-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: ncurses-devel, gcc-c++

%description
The HT editor is a file editor, viewer and analyzer for text, binary and
especially executables. It has support for the following formats: common
object file format (COFF), executable and linkable format (ELF), linear
executables (LE), standard dos executables (MZ), new executables (NE),
portable executables (PE32, PE64), java class files (CLASS).

%prep
%setup

%build
%configure \
	--program-prefix="%{?_program_prefix}"
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
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.8.0-1.2
- Rebuild for Fedora Core 5.

* Mon Aug 09 2004 Dries Verachtert <dries@ulyssis.org> 0.8.0-1
- Update to version 0.8.0.

* Sun May 02 2004 Dag Wieers <dag@wieers.com> - 0.7.5-2
- Cosmetic changes.
- Fixed --program-prefix problem for RH73 and older.

* Sat Mar 20 2004 Dries Verachtert <dries@ulyssis.org> 0.7.5-1
- Initial package
