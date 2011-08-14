Summary: Simple command line tool to display information about a data transfer stream
Name: bar
Version: 1.11.1
Release: 1
License: GPLv2
Group: Development/Tools
URL: http://clpbar.sourceforge.net/
Source: http://downloads.sourceforge.net/project/clpbar/clpbar/%{name}-%{version}/%{name}_%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
This is a simple command line tool to display information
about a data transfer stream.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS COPYING TODO
%{_bindir}/bar

%doc %attr(0444,root,root) %{_mandir}/man1/*.1.gz

%changelog
* Wed Aug 03 2010 Bjarne Saltbaek <arnebjarne72@hotmail.com> - 1.11.1-1
- Initial RPM release.
