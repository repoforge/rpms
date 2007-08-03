# $Id$
# Authority: dag
# Upstream: Mattia Barbon <mbarbon@cpan.org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Wx

Summary: interface to the wxWidgets cross-platform GUI toolkit
Name: perl-Wx
Version: 0.74
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Wx/

Source: http://www.cpan.org/modules/by-module/Wx/Wx-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(Test::More) >= 0.45
BuildRequires: perl(ExtUtils::MakeMaker) >= 6.17
BuildRequires: perl(Alien::wxWidgets) >= 0.25
BuildRequires: perl(Test::Harness) >= 2.26
BuildRequires: perl(File::Spec::Functions) >= 0.82
BuildRequires: perl(Data::Dumper)

%description
interface to the wxWidgets cross-platform GUI toolkit.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}/auto/*{,/*{,/*}}/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST MANIFEST.SKIP META.yml README.txt README.txt
%doc %{_mandir}/man3/Wx.3pm*
#%doc %{_mandir}/man3/*.3pm*
%{perl_vendorarch}/Wx.pm
%{perl_vendorarch}/auto/Wx/

%changelog
* Fri May 04 2007 Dag Wieers <dag@wieers.com> - 0.74-1
- Initial package. (using DAR)
