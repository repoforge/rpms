# $Id$
# Authority: dries
# Upstream: Ingy d&#246;t Net <INGY$cpan,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Data-Denter

Summary: Alternative to Data::Dumper and Storable.
Name: perl-Data-Denter
Version: 0.15
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Data-Denter/

Source: http://search.cpan.org/CPAN/authors/id/I/IN/INGY/Data-Denter-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
Data::Denter is yet another Perl data serializer/deserializer. It formats
nested data structures in an indented fashion. It is optimized for human
readability/editability, safe deserialization, and (eventually) speed.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Data/Denter.p*

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.15-1.2
- Rebuild for Fedora Core 5.

* Wed Dec 21 2005 Dries Verachtert <dries@ulyssis.org> - 0.15-1
- Initial package.
