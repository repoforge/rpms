# $Id$
# Authority: dag

Summary: Web server benchmark
Name: httperf
Version: 0.9.0
Release: 1%{?dist}
License: GPL
Group: Applications/Internet
URL: http://www.hpl.hp.com/research/linux/httperf/

Source: ftp://ftp.hpl.hp.com/pub/httperf/httperf-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: openssl-devel

%description
httperf is a popular web server benchmark tool for measuring web server
performance. It provides a flexible facility for generating various HTTP
workloads and for measuring server performance. The focus of httperf is
not on implementing one particular benchmark but on providing a robust,
high-performance tool that  facilitates the construction of both micro-
and macro-level benchmarks. The three distinguishing characteristics of
httperf are its robustness, which includes the ability to generate and
sustain server overload, support for the HTTP/1.1 protocol, and its 
extensibility to new workload generators and performance measurements. 

%prep
%setup

%build
%configure \
    --program-prefix="%{?_program_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog NEWS README TODO
%doc %{_mandir}/man1/httperf.1*
%{_bindir}/httperf
%{_bindir}/idleconn

%changelog
* Fri Aug 17 2007 Dag Wieers <dag@wieers.com> - 0.9.0-1
- Initial package. (using DAR)
