# $Id: _template.spec 219 2004-04-09 06:21:45Z dag $
# Authority: dag
# Upstream: Sebastiano Vigna <vigna$dsi,unimi,it>

Summary: Nice editor
Name: ne
Version: 1.32
Release: 1
License: GPL
Group: Applications/Editors
URL: http://ne.dsi.unimi.it/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://ne.dsi.unimi.it/ne-%{version}.tar.gz
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: ncurses-devel >= 4.0

%description 
ne is a free (GPL'd) text editor based on the POSIX standard that runs (we
hope) on almost any UN*X machine. ne is easy to use for the beginner, but
powerful and fully configurable for the wizard, and most sparing in its
resource usage. If you have the resources and the patience to use emacs or the
right mental twist to use vi then probably ne is not for you. However, being
fast, small, powerful and simple to use, ne is ideal for email, editing through
phone line (or slow GSM/GPRS) connections and so on. Moreover, the internal
text representation is very compact--you can easily load and modify very large
files.

%package docs
Summary: Documentation for package %{name}
Group: Documentation

%description docs
This package includes the documentation for package %{name}.

%prep
%setup

%build
%{__make} %{?_smp_mflags} -C src \
	CFLAGS="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__install} -D -m0755 src/ne %{buildroot}%{_bindir}/ne
%{__install} -D -m0644 doc/ne.1 %{buildroot}%{_mandir}/man1/ne.1

%{__install} -d -m0755 %{buildroot}%{_infodir}
%{__install} -D -m0644 doc/ne.info* %{buildroot}%{_infodir}

%post
/sbin/install-info %{_infodir}/%{name}.info.gz %{_infodir}/dir

%preun
/sbin/install-info --delete %{_infodir}/%{name}.info.gz %{_infodir}/dir

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES COPYING README doc/default.* doc/*.html doc/ne.txt terms/
%doc %{_mandir}/man?/*
%doc %{_infodir}/*.info*
%{_bindir}/*

%files docs
%defattr(-, root, root, 0755)
%doc doc/*.html doc/*.pdf doc/*.ps doc/ne.txt

%changelog
* Sun Apr 18 2004 Dag Wieers <dag@wieers.com> - 1.32-1
- Initial package. (using DAR)
