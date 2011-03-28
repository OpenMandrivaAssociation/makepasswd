%define name 	makepasswd
%define version 0.5.0
%define release %mkrel 1

Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Summary: 	Generate random passwords
License: 	GPL
Group: 		System/Configuration/Other
URL: 		http://www.defora.org/index.php?page=projects&project=makepasswd
Source0: 	http://www.defora.org/os/download/3500/%{name}-%{version}.tar.gz
BuildRoot: 	%{_tmppath}/%{name}-%{version}

%description
Makepasswd generates pseudo-random passwords of a desired length. It is able
to generate its crypted equivalent.

%prep
%setup -q

%build
%make CFLAGS="%{optflags}"

%install
rm -fr %{buildroot}
%makeinstall PREFIX=%{buildroot}%{_prefix}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/makepasswd
