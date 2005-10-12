# $Id$

# Authority: dries
# Upstream: Benjamin Trott <cpan$stupidfool,org>


%define real_name Digest-BubbleBabble
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Create bubble-babble fingerprints
Name: perl-Digest-BubbleBabble
Version: 0.01
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Digest-BubbleBabble/

Source: http://www.cpan.org/modules/by-module/Digest/Digest-BubbleBabble-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
This module allows you to create bubble-babble fingerprints.

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
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/Digest/BubbleBabble.pm

%changelog
* Wed Jun 16 2004 Dries Verachtert <dries@ulyssis.org> - 0.01-1
- Initial package.
