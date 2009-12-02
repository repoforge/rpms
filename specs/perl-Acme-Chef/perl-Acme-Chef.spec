# $Id$
# Authority: shuff
# Upstream: Steffen Mueller <chef-module$steffen-mueller,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Acme-Chef

Summary: An interpreter for the Chef programming language
Name: perl-%{real_name}
Version: 1.01
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Acme-Chef/

Source: http://search.cpan.org/CPAN/authors/id/S/SM/SMUELLER/Acme-Chef-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(File::Temp)
BuildRequires: perl(Test::Pod)
BuildRequires: perl(Test::Pod::Coverage)
Requires: perl


%description
Chef is an esoteric programming language in which programs look like recipes. I
needn't mention that using it in production environment, heck, using it for
anything but entertainment ought to result in bugs and chaos in reverse order.

All methods provided by Acme::Chef are adequately described in the synopsis. If
you don't think so, you need to read the source code.

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
%doc Changes MANIFEST META.yml README
%doc examples
%doc %{_mandir}/man?/*
%dir %{perl_vendorlib}/Acme/
%{perl_vendorlib}/Acme/*
%{_bindir}/

%changelog
* Wed Dec 02 2009 Steve Huff <shuff@vecna.org> - 1.01-1
- Initial package.
