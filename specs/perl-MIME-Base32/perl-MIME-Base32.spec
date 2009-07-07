# $Id$
# Authority: cmr
# Upstream: Daniel Peder <Daniel,Peder$INFOSET,cz>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name MIME-Base32

Summary: Perl module named MIME-Base32
Name: perl-MIME-Base32
Version: 1.01
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/MIME-Base32/

Source: http://www.cpan.org/modules/by-module/MIME/MIME-Base32-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-MIME-Base32 is a Perl module.

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
%doc MANIFEST META.yml README
%doc %{_mandir}/man3/MIME::Base32.3pm*
%dir %{perl_vendorlib}/MIME/
%{perl_vendorlib}/MIME/test1.pl
%{perl_vendorlib}/MIME/Base32.pm

%changelog
* Tue Jul 07 2009 Christoph Maser <cmr@financial.com> - 1.01-1
- Initial package. (using DAR)
