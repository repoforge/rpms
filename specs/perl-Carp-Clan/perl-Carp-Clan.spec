# $Id$

# Authority: dries
# Upstream: Steffen Beyer <sb$engelschall,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Carp-Clan

Summary: Report errors which match a pattern
Name: perl-Carp-Clan
Version: 5.3
Release: 1
License: GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Carp-Clan/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://www.cpan.org/modules/by-module/Carp/Carp-Clan-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
This module reports errors from the perspective of the caller of a
"clan" of modules, similar to "Carp.pm" itself. But instead of giving
it a number of levels to skip on the calling stack, you give it a
pattern to characterize the package names of the "clan" of modules
which shall never be blamed for any error.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod
%{__rm} -f %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README.txt CHANGES.txt GNU_GPL.txt
%{_mandir}/man3/*
%{perl_vendorlib}/Carp/Clan.pm
%{perl_vendorlib}/Carp/Clan.pod

%changelog
* Wed Jun 16 2004 Dries Verachtert <dries@ulyssis.org> - 5.3-1
- Initial package.
