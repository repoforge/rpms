# $Id$
# Authority: dag
# Upstream: Christian Lackas <delta$lackas,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Digest-Perl-MD5

Summary: Perl module that implements Ron Rivests MD5 Algorithm
Name: perl-Digest-Perl-MD5
Version: 1.8
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Digest-Perl-MD5/

Source: http://www.cpan.org/modules/by-module/Digest/Digest-Perl-MD5-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-Digest-Perl-MD5 is a Perl module that implements Ron Rivests MD5 Algorithm.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES INSTALL MANIFEST META.yml README
%doc %{_mandir}/man3/Digest::Perl::MD5.3pm*
%dir %{perl_vendorlib}/Digest/
%dir %{perl_vendorlib}/Digest/Perl/
%{perl_vendorlib}/Digest/Perl/MD5.pm

%changelog
* Sun Oct 07 2007 Dag Wieers <dag@wieers.com> - 1.8-1
- Initial package. (using DAR)
