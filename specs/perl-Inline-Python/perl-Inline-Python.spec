# $Id$

# Authority: dries
# Upstream: Neil Watkiss <nwatkiss$ttul,org>

%define real_name Inline-Python
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Write Perl subs and classes in Python
Name: perl-Inline-Python
Version: 0.20
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Inline-Python/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://search.cpan.org/CPAN/authors/id/N/NE/NEILW/Inline-Python-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
Inline::Python lets you write Perl subroutines and classes in
Python. You don't have to use any funky techniques for sharing most
types of data between the two languages, either. Inline::Python comes
with its own data translation service. It converts any Python structures
it knows about into Perl structures, and vice versa. 

%prep
%setup -n %{real_name}-%{version}

%build
echo 1 | %{__perl} Makefile.PL INSTALLDIRS="vendor" destdir=%{buildroot}
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README Changes
%doc %{_mandir}/man3/*
%{perl_vendorarch}/Inline/Python.*
%{perl_vendorarch}/auto/Inline/Python/*
%exclude %{perl_archlib}/perllocal.pod
%exclude %{perl_vendorarch}/auto/*/*/.packlist

%changelog
* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 0.20-1
- Initial package.
