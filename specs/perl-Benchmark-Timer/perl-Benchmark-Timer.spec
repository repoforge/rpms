# $Id$
# Authority: shuff
# Upstream: David Coppit <david$coppit,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Benchmark-Timer

Summary: Benchmarking with statistical confidence
Name: perl-%{real_name}
Version: 0.7102
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Benchmark-Timer/

Source: http://search.cpan.org/CPAN/authors/id/D/DC/DCOPPIT/Benchmark-Timer-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: perl >= 5.005
#BuildRequires: perl(ExtUtils::MakeMaker) >= 6.42
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Statistics::PointEstimation)
BuildRequires: perl(Time::HiRes)
BuildRequires: rpm-macros-rpmforge
Requires: perl >= 5.005
Requires: perl(Time::HiRes)
Requires: perl(Statistics::PointEstimation)

Provides: %{name} = %{version}
Provides: perl(Benchmark::Timer) = %{version}

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_from_provides /^perl.*/d
%filter_setup

%description
The Benchmark::Timer class allows you to time portions of code conveniently, as
well as benchmark code by allowing timings of repeated trials. It is perfect
for when you need more precise information about the running time of portions
of your code than the Benchmark module will give you, but don't want to go all
out and profile your code.

The methodology is simple; create a Benchmark::Timer object, and wrap portions
of code that you want to benchmark with start() and stop() method calls. You
can supply a tag to those methods if you plan to time multiple portions of
code. If you provide error and confidence values, you can also use
need_more_samples() to determine, statistically, whether you need to collect
more data.

After you have run your code, you can obtain information about the running time
by calling the results() method, or get a descriptive benchmark report by
calling report(). If you run your code over multiple trials, the average time
is reported. This is wonderful for benchmarking time-critical portions of code
in a rigorous way. You can also optionally choose to skip any number of initial
trials to cut down on initial case irregularities.

%prep
%setup -n %{real_name}-%{version}

# fix the shebang
sed -i -e 's/^#!\/usr\/local\/bin\/perl/#!\/usr\/bin\/perl/' delta.pl

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

%{__install} -d %{buildroot}%{_bindir}
%{__install} -m 0755 delta.pl %{buildroot}%{_bindir}

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES MANIFEST LICENSE README
%doc %{_mandir}/man3/*
%dir %{perl_vendorlib}/Benchmark/
%{perl_vendorlib}/Benchmark/*
%{_bindir}/delta.pl

%changelog
* Fri Nov 13 2009 Steve Huff <shuff@vecna.org> - 0.7102-1
- Initial package.
