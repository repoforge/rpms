# Authority: dag

%define rversion 1.0b1

Summary: A Linux Hotline Client with almost full 1.5 compatibility.
Name: fidelio
Version: 1.0
Release: 0.b1
License: GPL
Group: Applications/Internet
URL: http://fidelio.sf.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/fidelio/fidelio-%{rversion}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

%description 
Fidelio is a Hotline compatible client that supports most of the features of
Hotline. Public chat, tranfsers, flat and threaded news, icons, sounds, and 
messages are supported. Banners, private chat, and the administrative 
functions are not. 

%prep
%setup -n %{name}-%{rversion}

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog NEWS README TODO
%{_bindir}/*
%{_datadir}/fidelio.default

%changelog
* Mon Feb 10 2003 Dag Wieers <dag@wieers.com> - 1.0-0.b1
- Initial package. (using DAR)
