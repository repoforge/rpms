# $Id$
# Authority: dries
# Upstream: Adam Kennedy <cpan$al,as>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Config-Tiny

Summary: Read and write ini style files
Name: perl-Config-Tiny
Version: 2.10
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Config-Tiny/

Source: http://www.cpan.org/modules/by-module/Config/Config-Tiny-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(Test::More) >= 0.47, perl(FindBin) >= 1.42

%description
Config::Tiny is a perl class to read and write .ini style configuration
files with as little code as possible, reducing load time and memory
overhead. Memory usage is normally scoffed at in Perl, but in my opinion
should be at least kept in mind.

This module is primarily for reading human written files, and anything
we write shouldn't need to have documentation/comments. If you need
something with more power, move up to Config::Simple, Config::General or
one of the many other Config:: modules. To rephrase, Config::Tiny does
not preserve your comments, whitespace, or the order of your config
file.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}/auto/*{,/*{,/*}}/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes LICENSE README
%doc %{_mandir}/man3/*
%dir %{perl_vendorlib}/Config/
%{perl_vendorlib}/Config/Tiny.pm

%changelog
* Tue Nov 14 2006 Dries Verachtert <dries@ulyssis.org> - 2.10-1
- Updated to release 2.10.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 2.08-1
- Updated to release 2.08.

* Fri Jun  2 2006 Dries Verachtert <dries@ulyssis.org> - 2.07-1
- Updated to release 2.07.

* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 2.05-1
- Updated to release 2.05.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 2.04-1.2
- Rebuild for Fedora Core 5.

* Sat Jan  7 2006 Dries Verachtert <dries@ulyssis.org> - 2.04-1
- Updated to release 2.04.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 2.02-1
- Updated to release 2.02.

* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 2.01-1
- Updated to release 2.01.

* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 2.00-1
- Initial package.
