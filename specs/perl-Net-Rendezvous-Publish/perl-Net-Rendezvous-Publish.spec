# $Id$

# Authority: dries
# Upstream: Richard Clamp <richardc$unixbeard,net>

%define real_name Net-Rendezvous-Publish
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Publish Rendezvous services
Name: perl-Net-Rendezvous-Publish
Version: 0.03
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-Rendezvous-Publish/

Source: http://search.cpan.org/CPAN/authors/id/R/RC/RCLAMP/Net-Rendezvous-Publish-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
With this module, you can publish Rendezvous services.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod
%{__rm} -f %{buildroot}%{perl_vendorarch}/auto/*/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Net/Rendezvous/Publish.pm
%{perl_vendorlib}/Net/Rendezvous/Publish/*

%changelog
* Fri Mar  4 2005 Dries Verachtert <dries@ulyssis.org> - 0.03-1
- Updated to release 0.03.

* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 0.01
- Initial package.
