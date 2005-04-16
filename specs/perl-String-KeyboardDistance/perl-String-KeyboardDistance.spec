# $Id$
# Authority: dries
# Upstream: Kyle R. Burton <kyle,burton$gmail,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name String-KeyboardDistance

Summary: String Comparison Algorithm
Name: perl-String-KeyboardDistance
Version: 1.01
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/String-KeyboardDistance/

Source: http://search.cpan.org/CPAN/authors/id/K/KR/KRBURTON/String-KeyboardDistance-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
This module implmements a version of keyboard distance for fuzzy string
matching. Keyboard distance is a measure of the physical distance
between two keys on a keyboard. For example, 'g' has a distance of 1
from the keys 'r', 't', 'y', 'f', 'h', 'v', 'b', and 'n'. Immediate
diagonals (like ''r, 'y', 'v', and 'n') are considered to have a
distance of 1 instead of 1.414 to help to prevent horizontal/vertical
bias.

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
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/String/KeyboardDistance.pm

%changelog
* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.01-1
- Initial package.
