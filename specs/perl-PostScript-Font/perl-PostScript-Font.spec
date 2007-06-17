# $Id$
# Authority: dries
# Upstream: Johan Vromans <jvromans$squirrel,nl>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name PostScript-Font

Summary: PostScript font functions
Name: perl-PostScript-Font
Version: 1.10
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/PostScript-Font/

Source: http://search.cpan.org/CPAN/authors/id/J/JV/JV/PostScript-Font-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
This package contains a couple of modules to get information for and
from PostScript fonts and associated metrics files. Also included is a
module to facilitate basic typesetting, a program to make font
samples, and programs to handle the conversion of font data to
PostScript binary (.pfb) and ASCII (.pfa) formats. Example program
shows how basic typesetting can be obtained.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES README
%doc %{_mandir}/man?/*
%{_bindir}/font2pfa
%{_bindir}/font2pfb
%{_bindir}/fontsampler
%{_bindir}/ttfwrapper
%{perl_vendorlib}/PostScript

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.10-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.10-1
- Initial package.
