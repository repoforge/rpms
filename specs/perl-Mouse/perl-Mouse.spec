# $Id$
# Authority: dag
# Upstream: Shawn M Moore <sartak$gmail,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Mouse

Summary: Moose minus the antlers
Name: perl-Mouse
Version: 0.40
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Mouse/

Source: http://search.cpan.org/CPAN/authors/id/G/GF/GFUJI/Mouse-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
#BuildRequires: perl(ExtUtils::MakeMaker) >= 6.42
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(ExtUtils::ParseXS) >= 2.21
BuildRequires: perl(File::Basename)
BuildRequires: perl(File::Path)
BuildRequires: perl(File::Spec)
BuildRequires: perl(Scalar::Util) >= 1.14
BuildRequires: perl(Test::Exception) >= 0.27
#BuildRequires: perl(Test::More) >= 0.88
BuildRequires: perl(Test::More)
BuildRequires: perl(XSLoader) >= 0.1
BuildRequires: perl >= 5.6.2
Requires: perl(MouseX::AttributeHelpers) >= 0.06
Requires: perl(Scalar::Util) >= 1.14
Requires: perl(XSLoader) >= 0.1
Requires: perl >= 5.6.2

%filter_from_requires /^perl*/d
%filter_setup

%description
Moose is wonderful. Use Moose instead of Mouse.

Unfortunately, Moose has a compile-time penalty. Though significant progress
has been made over the years, the compile time penalty is a non-starter for
some very specific applications. If you are writing a command-line application
or CGI script where startup time is essential, you may not be able to use
Moose. We recommend that you instead use HTTP::Engine and FastCGI for the
latter, if possible.

Mouse aims to alleviate this by providing a subset of Moose's functionality,
faster.

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
%doc %{_mandir}/man?/*
%{perl_vendorlib}/Mouse/
%{perl_vendorlib}/Mouse.pm
%{perl_vendorlib}/ouse.pm
%{perl_vendorlib}/Squirrel/
%{perl_vendorlib}/Squirrel.pm


%changelog
* Tue Jun 01 2010 Steve Huff <shuff@vecna.org> - 0.40-1
- Updated to version 0.40.
- Package has new maintainer, old spec wouldn't build.

* Wed Sep  9 2009 Christoph Maser <cmr@financial.com> - 0.28-1
- Updated to version 0.28.

* Sat Jul  4 2009 Christoph Maser <cmr@financial.com> - 0.27-1
- Updated to version 0.27.

* Thu Oct 09 2008 Dag Wieers <dag@wieers.com> - 0.09-1
- Initial package. (using DAR)
