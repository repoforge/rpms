# $Id$

# Authority: dries
# Upstream: Jeremy Muhlich <jmuhlich%20at%20bitflood,org>

%define real_name Net-IRC
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

Summary: Perl interface to the Internet Relay Chat protocol
Name: perl-Net-IRC
Version: 0.75
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-IRC/

Source: http://www.cpan.org/modules/by-module/Net/Net-IRC-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
First intended to be a quick tool for writing an IRC script in Perl, 
Net::IRC has grown into a comprehensive Perl implementation of the IRC 
protocol (RFC 1459).

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX=%{buildroot}%{_prefix}
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
%{perl_vendorlib}/Net/IRC.pm
%{perl_vendorlib}/Net/IRC

%changelog
* Sun Mar  6 2005 Dries Verachtert <dries@ulyssis.org> - 0.75-1
- Initial package.
