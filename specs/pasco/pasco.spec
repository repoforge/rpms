# $Id$
# Authority: dag

Summary: pasco
Name: pasco
Version: 1.0
Release: 1%{?dist}
License: GPL
Group: Applications/File
URL: http://www.foundstone.com/us/resources/proddesc/pasco.htm

Source: pasco-1.0.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++
BuildRequires: libstdc++-devel

%description
Pasco will parse the information in an index.dat file and output the
results in a field delimited manner so that it may be imported into
your favorite spreadsheet program. Pasco is built to work on multiple
platforms and will execute on Windows (through Cygwin), Mac OS X, Linux,
and *BSD platforms.

%prep
%setup -n %{name}

%build
%{__make} -C src %{?_smp_mflags}

%install
%{__install} -Dp -m755 src/pasco %{buildroot}%{_bindir}/pasco

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Readme.txt
%{_bindir}/pasco

%changelog
* Wed Feb 16 2011 Dag Wieers <dag@wieers.com> - 1.0-1
- Initial package. (using DAR)
