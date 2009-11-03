# $Id $
# Authority: dries

Summary: Print source code in a variety of languages to postscript
Name: trueprint
Version: 5.3
Release: 1.2%{?dist}
License: GPL
Group: Applications/Text
URL: http://www.gnu.org/software/trueprint/trueprint.html

Source: http://ftp.gnu.org/gnu/trueprint/trueprint-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: cups

%description
GNU Trueprint takes C source files and other text files and prints them on
PostScript printers. It is intended to be used by programmers; therefore, it
includes features like diff-marking, indentation count, function and file
indices, and many others that are useful when printing source code.

It currently supports C and has more limited support for other languages,
including C++, Java, and Perl.

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
%doc AUTHORS COPYING NEWS README
%doc %{_infodir}/*.info*
%doc %{_mandir}/man?/*
%{_bindir}/trueprint

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 5.3-1.2
- Rebuild for Fedora Core 5.

* Thu Apr 22 2004 Dries Verachtert <dries@ulyssis.org> 5.3-1
- Initial package
