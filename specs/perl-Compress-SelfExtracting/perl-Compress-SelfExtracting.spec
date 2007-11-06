# $Id$
# Authority: dries
# Upstream: Sean O'Rourke <educated%20underscore%20foo%20at%20yahoo%20dot%20com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Compress-SelfExtracting

Summary: Create compressed scripts
Name: perl-Compress-SelfExtracting
Version: 0.04
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Compress-SelfExtracting/

Source: http://search.cpan.org/CPAN/authors/id/S/SE/SEANO/Compress-SelfExtracting-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(ExtUtils::MakeMaker), perl

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
%{__make} install
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Compress/SelfExtracting.pm
%{perl_vendorlib}/Compress/SelfExtracting

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.04-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.04-1
- Initial package.
