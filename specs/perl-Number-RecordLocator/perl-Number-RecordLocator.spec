# $Id$
# Authority: shuff
# Upstream: Jesse Vincent <jesse$bestpractical,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Number-RecordLocator

Summary: Encodes integers into a short and easy to read and pronounce "locator string"
Name: perl-%{real_name}
Version: 0.005
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Number-RecordLocator/

Source: http://search.cpan.org/CPAN/authors/id/J/JE/JESSE/Number-RecordLocator-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Test::More)


%description
Number::RecordLocator encodes integers into a 32 character "alphabet" designed
to be short and easy to read and pronounce. The encoding maps:

    0 to O
    1 to I
    S to F 
    B to P

With a 32 bit encoding, you can map 33.5 million unique ids into a 5 character
code.


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
%doc Changes MANIFEST META.yml README SIGNATURE
%doc %{_mandir}/man3/*
%dir %{perl_vendorlib}/Number/
%{perl_vendorlib}/Number/*

%changelog
* Mon Oct 05 2009 Steve Huff <shuff@vecna.org> - 0.005-1
- Initial package.

