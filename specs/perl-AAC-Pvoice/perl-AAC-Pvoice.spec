# $Id$
# Authority: dag
# Upstream: Jouke Visser <jouke$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name AAC-Pvoice

Summary: Perl module to create GUI software for disabled people
Name: perl-AAC-Pvoice
Version: 0.91
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/AAC-Pvoice/

Source: http://www.cpan.org/authors/id/J/JO/JOUKE/AAC-Pvoice-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-AAC-Pvoice is a Perl module to create GUI software for disabled people.

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
%doc Changes LICENSE MANIFEST META.yml README Todo
%doc %{_mandir}/man3/AAC::Pvoice.3pm*
%doc %{_mandir}/man3/AAC::Pvoice::*.3pm*
%dir %{perl_vendorlib}/AAC/
%{perl_vendorlib}/AAC/Pvoice/
%{perl_vendorlib}/AAC/Pvoice.pm

%changelog
* Sun Aug 05 2007 Dag Wieers <dag@wieers.com> - 0.91-1
- Initial package. (using DAR)
