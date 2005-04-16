# $Id$
# Authority: dries
# Upstream: Sean O'Rourke <educated%20underscore%20foo%20at%20yahoo%20dot%20com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Compress-SelfExtracting

Summary: Create compressed scripts
Name: perl-Compress-SelfExtracting
Version: 0.04
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Compress-SelfExtracting/

Source: http://search.cpan.org/CPAN/authors/id/S/SE/SEANO/Compress-SelfExtracting-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Compress::SelfExtracting allows you to create pure-Perl
self-extracting scripts using a variety of compression algorithms.
These scripts will then run on any system with a recent version of
Perl.

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
%{perl_vendorlib}/Compress/SelfExtracting.pm
%{perl_vendorlib}/Compress/SelfExtracting

%changelog
* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.04-1
- Initial package.
