# $Id$

# Authority: dries
# Upstream: Ray Finch <finchray$yahoo,com>

%define real_name Clone
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Recursively copy Perl datatypes
Name: perl-Clone
Version: 0.15
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Clone/

Source: http://search.cpan.org/CPAN/authors/id/R/RD/RDF/Clone-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
With this module, you can recursively copy Perl datatypes.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" destdir=%{buildroot}
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes
%doc %{_mandir}/man3/*
%{perl_vendorarch}/Clone.pm
%{perl_vendorarch}/auto/Clone
%exclude %{perl_archlib}/perllocal.pod
%exclude %{perl_vendorarch}/auto/*/.packlist

%changelog
* Tue Dec 07 2004 Dries Verachtert <dries@ulyssis.org> - 0.15-1
- Initial package.
