# $Id$
# Authority: cmr
# Upstream: Simon Wistow <simon$thegestalt,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Net-Google-AuthSub

Summary: interact with sites that implement Google style AuthSub
Name: perl-Net-Google-AuthSub
Version: 0.5
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-Google-AuthSub/

Source: http://www.cpan.org/modules/by-module/Net/Net-Google-AuthSub-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
interact with sites that implement Google style AuthSub.

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
%doc Changes MANIFEST META.yml
%doc %{_mandir}/man3/Net::Google::AuthSub*.3pm*
%dir %{perl_vendorlib}/Net/
%dir %{perl_vendorlib}/Net/Google/
%{perl_vendorlib}/Net/Google/AuthSub/
%{perl_vendorlib}/Net/Google/AuthSub.pm

%changelog
* Wed Jul 08 2009 Christoph Maser <cmr@financial.com> - 0.5-1
- Initial package. (using DAR)
