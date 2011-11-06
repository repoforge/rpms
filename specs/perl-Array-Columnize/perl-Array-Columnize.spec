# Upstream: Rocky Bernstein <rocky@scpan.org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Array-Columnize

Summary: Arrange list data in columns
Name: perl-%{real_name}
Version: v0.3.8
Release: 1%{?dist}
License: GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Array-Columnize/

Source: http://www.cpan.org/authors/id/R/RO/ROCKY/Array-Columnize-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Module::Build)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(ExtUtils::PkgConfig)
BuildRequires: perl(Test::More)
BuildRequires: perl(version)
Requires: perl

%filter_from_requires /^perl*/d
%filter_setup

%description
In showing long lists, sometimes one would prefer to see the values arranged and aligned in columns. Some examples include listing methods of an object, listing debugger commands, or showing a numeric array with data aligned.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Build.PL --installdirs vendor --destdir %{buildroot}
./Build

%install
%{__rm} -rf %{buildroot}
./Build pure_install
%{__rm} -rvf %{_mandir}/man3/Array::Columnize::options.3pm*

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.json README.md
%doc %{_mandir}/man3/Array::Columnize.3pm*
%doc %{_mandir}/man3/Array::Columnize::options.3pm*
%dir %{perl_vendorlib}/Array/
%{perl_vendorlib}/Array/Columnize.pm
%{perl_vendorlib}/Array/Columnize/columnize.pm
%{perl_vendorlib}/Array/Columnize/options.pm

%changelog
* Sat Nov 05 2011 Rocky Bernstein <rocky@cpan.org> - 0.38-1
- Initial package.
