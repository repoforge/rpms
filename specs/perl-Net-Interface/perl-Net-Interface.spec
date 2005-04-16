# $Id$
# Authority: dries
# Upstream: Jerrad Pierce <jpierce$cpan,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Net-Interface

Summary: Access network interfaces
Name: perl-Net-Interface
Version: 0.04_2
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-Interface/

Source: http://search.cpan.org/CPAN/authors/id/J/JP/JPIERCE/Net-Interface-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
Net::Interface is designed to make the use of ifconfig(1) and friends
unnecessary from within Perl.  It provides methods to get at set all
the attributes of an interface, and even create new logical or
physical interfaces (if your O/S supports it).

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorarch}/Net/Interface.pm
%{perl_vendorarch}/auto/Net/Interface

%changelog
* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.04_2-1
- Initial package.
